import sqlalchemy as _sql
import json
import zlib
import bookapp.database as _database


class CompressedJSON(_sql.types.TypeDecorator):
    impl = _sql.types.LargeBinary

    def process_result_value(self, value, dialect):
        if value is None:
            return []
        res = json.loads(zlib.decompress(value).decode("utf-8"))
        return res


class Recommendations(_database.Base):
    __tablename__ = "recommendations"
    id = _sql.Column("id", _sql.Integer, primary_key=True, index=True)
    history = _sql.Column(CompressedJSON)
    recommendations = _sql.Column(CompressedJSON, default=[])


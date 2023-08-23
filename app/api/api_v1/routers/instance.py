from fastapi import APIRouter, Depends, status, HTTPException, Response
from app.schemas.mongo_instance import MongoInstance, MongoInstanceCreate
from app.db.mysql.session_local import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, StatementError, OperationalError
from app.core.server.instance import create_mongodb_instance
from loguru import logger

router = APIRouter()


@router.post('/instance',
             status_code=status.HTTP_201_CREATED,
             response_model=MongoInstance, )
async def add_mongo_instance(instance: MongoInstanceCreate, db: Session = Depends(get_db)):
    try:
        create_mongodb_instance(instance, db)
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e.orig))
    except (SQLAlchemyError, StatementError, OperationalError) as e:
        logger.error(e.orig)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e.orig))
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return instance

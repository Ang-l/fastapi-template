
import uuid
from datetime import datetime


from pydantic import BaseModel
from typing import Optional


# Return the basic class
class ResponseBaseModel(BaseModel):    
    code: Optional[int] = 10200
    msg: Optional[str] = "success"

    # Adding additional information is not necessary
    data: Optional[datetime] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    TrackId: Optional[str] = uuid.uuid4().hex


class CreateResponseModel(ResponseBaseModel):
    ...


class UpdateResponseModel(ResponseBaseModel):
    ...
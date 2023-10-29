from fastapi import FastAPI

sub_app = FastAPI()


@sub_app.get("/subappendpoint")
def subpp_endpoint():
    return {"message": "This is a sub-app endpoint"}

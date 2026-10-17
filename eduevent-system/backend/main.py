from fastapi import FastAPI


# from identity.router import router as identity_router
# from events.router import router as events_router
# from discovery.router import router as discovery_router
# from enrollment.router import router as enrollment_router
# from operations.router import router as operations_router
# from notifications.router import router as notifications_router

app = FastAPI(
    title="EduEvent System API",
    description="Główny backend do zarządzania wydarzeniami na uczelni",
    version="1.0.0"
)

# app.include_router(identity_router, prefix="/identity", tags=["Identity & Authentication"])
# app.include_router(events_router, prefix="/events", tags=["Events Management"])
# app.include_router(discovery_router, prefix="/discovery", tags=["Discovery & Search"])
# app.include_router(enrollment_router, prefix="/enrollment", tags=["Enrollment & Limits"])
# app.include_router(operations_router, prefix="/operations", tags=["On-site Operations"])
# app.include_router(notifications_router, prefix="/notifications", tags=["Notifications"])

@app.get("/")
def root():
    return {"message": "Welcome to API EduEvent!"}
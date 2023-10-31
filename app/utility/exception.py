from fastapi.responses import JSONResponse


def handle_exceptions(original_fn):
    async def wrapper_fn(*args, **kwargs):
        try:
            return await original_fn(*args, **kwargs)
        except Exception as e:
            return JSONResponse(
                content={"error": str(e)},
                status_code=500,
            )

    return wrapper_fn

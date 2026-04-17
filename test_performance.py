import pytest
import asyncio
import time
import httpx

from api_pagamentos import app


@pytest.mark.asyncio
@pytest.mark.parametrize("quantidade", [5, 20, 50])
async def test_performance(quantidade):
    
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:

        inicio = time.perf_counter()

        tasks = [
            client.get("/processar")
            for _ in range(quantidade)
        ]

        responses = await asyncio.gather(*tasks)

        fim = time.perf_counter()
        tempo_total = fim - inicio

        for response in responses:
            assert response.status_code == 200

        assert tempo_total < 3.5, f"Tempo muito alto: {tempo_total}s"
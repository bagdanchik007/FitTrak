# Architecture layers (short)

1. **API** (`app/api`) – FastAPI routers, HTTP only  
2. **Application** (`app/application`) – use cases / services / DTOs  
3. **Domain** (`app/domain`) – entities & pure logic  
4. **Infrastructure** (`app/infrastructure`) – SQLAlchemy, repositories, mappers  

Dependencies point inward: API → Application → Domain ← Infrastructure.

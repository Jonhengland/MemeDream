# MemeDream
Memedream is a backend-focused social media platform for sharing and discovering memes, built with an emphasis on scalability, maintainability, and cloud-native design.

The system uses a hybrid backend architecture:

- Django as the core API layer for authentication, user management, and administrative capabilities
- Flask-based microservices to encapsulate domain-specific functionality such as meme publishing, feed generation, and user reactions
- AWS DynamoDB for horizontally scalable, low-latency data storage
- JWT-based authentication to support stateless, service-oriented communication
- AWS CDK for infrastructure-as-code and repeatable cloud deployments
  
The architecture prioritizes:

- Clear separation of concerns
- Horizontally scalable service boundaries
- Event-driven design patterns
- AWS-native primitives suitable for high-throughput workloads

Memedream is developed as a portfolio and learning project, with the goal of modeling production-grade backend systems and demonstrating sound system design practices applicable to large-scale social platforms.

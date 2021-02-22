# Architecture

## -Ilities Chart

| Ility               | Value | Reasoning |
| ------------------- |:-----:| --------- |
| Performance         |   2   | It is important that the database requests run quickly, but otherwise the largest performance bottleneck is the user themselves. |
| Security            |   2   | Care must be taken with passwords and credit card information, but otherwise most information is not at risk. |
| Safety              |   2   | Concerns for safety are low, there are no parts which can harm humans in the system. |
| Availability        |   3   | The database needs to be accessible at all times, and users should always be able to log in. |
| Maintainability     |   2   | The project needs to be fixable as new features are added, but the end product will not need to be changed very much. |
| Reliability         |   2   | The database cannot fail, so that part of the program needs to be well protected. Other parts of the program need to be generally reliable, but it isn't critical |
| Scalability         |   2   | As more clients are added, the software needs to be able to handle the many connections. It is important that it can scale to a point, but it's not likely that it will need to scale to website levels of clients. |
| Portability         |   2   | The platform for both the clients and the server are pre-determined, so we don't need to worry about supporting many platforms. |
| Usability           |   2   | Clients can be trained on how to use the software, so the software does not need to be incredibly easy to pick up, just easy to understand after being trained. |
| Supportability      |   2   | The software needs to be fixable when clients have issues. 24/7 support isn't necessary, but some general access is. |
| Re-configureability |   2   | Users need to be able to reassign admins and reconfigure things like menus, but the key data backing the client's views should not be modifiable (like database tables). |

# App shell (laptop + phone)

One React frontend, two layouts — **same routes and API**.

| Surface | Layout |
|---------|--------|
| **Laptop / desktop** (`lg+`) | Persistent left sidebar with all sections |
| **Phone / tablet** | Bottom tab bar (Home, Train, Coach, Live, More) + sheet for secondary pages |

PWA (`manifest` + service worker) allows “Add to Home Screen” so the mobile shell feels like an installed app.

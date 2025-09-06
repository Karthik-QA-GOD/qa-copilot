qa-copilot/
│── backend/                  # FastAPI app
│   │── app/
│   │   │── __init__.py
│   │   │── main.py           # Entry point (FastAPI routes)
│   │   │── models.py         # Pydantic models (Request/Response)
│   │   │── services.py       # Business logic (AI calls, formatting)
│   │   │── config.py         # API keys, settings
│   │   │── utils.py          # Helper functions
│   │── tests/
│   │   │── test_api.py       # Unit tests for endpoints
│   │── requirements.txt      # Python dependencies
│   │── README.md
│
│── frontend/                 # React app
│   │── public/
│   │── src/
│   │   │── components/       # Reusable UI components
│   │   │── pages/            # Pages (Home, Dashboard, etc.)
│   │   │── App.js
│   │   │── index.js
│   │── package.json
│   │── README.md
│
│── docs/                     # Documentation
│   │── architecture.md       # High-level design
│   │── roadmap.md            # Phases, milestones
│
│── .gitignore
│── README.md                 # Root project readme

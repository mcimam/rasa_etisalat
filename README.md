# Etisalat Chatbot
This project uses [Rasa](https://rasa.com/) for building conversational AI assistants.

## Description
This repository contains training data or at lest base of it for customer service chatbot. It comply with rasa open source 3.0 syntax. Please see oss documentation instead of rasa documentation. [Rasa OSS Documentation](https://legacy-docs-oss.rasa.com/docs/rasa/)


## Visualize Stories

To visualize your Rasa stories, generate the graph and open `graph.html`:

```bash
rasa visualize --out graph.html --domain data/domain
```

Open `graph.html` in your browser to explore the conversation paths.

## Installation

1. Clone the repository:
    ```bash
    git clone <repo-url>
    cd <project-directory>
    ```
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install rasa
    ```

## Training the Model

Train your assistant with:

```bash
rasa train --domanin=data/domain
```

To interactively check you model, run with:
```bash
rasa interactive --domain=data/domain
```

## Test model

To run the assistant locally:

1. Run actions server
```bash
rasa run actions
```

2. Run models
in separata terminal
```bash
rasa shell
```

For deployment options, refer to the [Rasa Deployment Guide](https://rasa.com/docs/rasa/deployment/).

## Author
[mcimam](https://github.com/mcimam)
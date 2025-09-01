TEXT-BASED FLOW DESCRIPTION

    START
    |
    ├── Initialize Chatbot
    |     │
    |     ├── Set up exit commands
    |     ├── Set up positive/negative word lists
    |     ├── Define available commands
    |     └── Prepare response lists
    |
    ├── Display Welcome Message
    |
    └── REPEAT UNTIL EXIT COMMAND:
          |
          ├── Get user input
          |
          ├── PROCESS INPUT:
          |     |
          |     ├── Check if exit command → Exit program
          |     ├── Check if greeting → Return random greeting
          |     ├── Check if known command → Execute command
          |     └── Otherwise → Return "unknown command" response
          |
          ├── ANALYZE SENTIMENT:
          |     |
          |     ├── Count positive words
          |     ├── Count negative words
          |     └── Determine overall sentiment
          |
          ├── RESPOND TO SENTIMENT:
          |     |
          |     ├── Positive → Show happy response
          |     ├── Negative → Show empathetic response
          |     └── Neutral → Continue
          |
          └── Loop back for next input

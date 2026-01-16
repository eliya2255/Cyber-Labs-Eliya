# Password Agent

## 1. Agent Name
**Password Agent**

## 2. Agent Purpose
The agent evaluates password security using a specific tool to measure length and safety status.

## 3. Agent Tools
- `check_password_strength(password)`: Returns the length of the string and a safety boolean.

## 4. Example Interaction
User: "Check if 'qwerty' is a good password."
Agent: (Calls tool) "No, it is only 6 characters long and is not considered safe."
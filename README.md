# Water Management System - DAJER (Hackathon Project)

A web application developed for the Malackathon 2024 hackathon, aimed at visualizing and managing water reservoir data to support sustainable water management solutions.

## Table of Contents
1. [Overview](#overview)
2. [Challenge Requirements](#challenge-requirements)
   - [Phase 1: Data Management](#phase-1-data-management)
   - [Phase 2: Web Application](#phase-2-web-application)
   - [Phase 3: Data Model Modification (not completed)](#phase-3-data-model-modification-not-completed)
   - [Phase 4: Predictive Model Development](#phase-4-predictive-model-development)
   - [Phase 5: Model Optimization and Water Transfer Solution](#phase-5-model-optimization-and-water-transfer-solution)
   - [Evaluation Criteria](#evaluation-criteria)
3. [Development Process](#development-process)
4. [Areas for Improvement](#areas-for-improvement)
5. [Website and More](#website-and-more)
   - [How to Use the Web Application](#how-to-use-the-web-application)
6. [Team Members](#team-members)

## Overview
The project was developed as part of the Malackathon 2024, an event organized by the School of Computer Science at the University of Málaga to address the challenges related to water sustainability (aligned with the United Nations' Sustainable Development Goal 6). The goal was to create a system that accesses a database hosted on Oracle Cloud Infrastructure (OCI) to retrieve information about water reservoirs and visualize it through an interactive map.

Our team had approximately 8 hours to develop the solution, excluding breaks for meals and the final presentation. Despite the time constraints, we successfully implemented most of the challenge phases, except for phase 3, which was not completed due to a lack of additional data available online.

## Challenge Requirements
The hackathon challenge consisted of five phases. Our implementation covered the following:

### Phase 1: Data Management
- We loaded the provided dataset into an Oracle Autonomous Database instance on OCI. The dataset focused on reservoirs located in Andalusia, and we created two key tables:
  - **Reservoir Details Table**: Contains information such as reservoir name, capacity, and geographical coordinates.
  - **Metadata Table**: Stores additional information, such as water levels over time, associated river basins, and administrative regions.
- We established relationships between these tables to create a robust relational model, enabling efficient queries and analysis.

### Phase 2: Web Application
- Developed a secure, mobile-accessible web application that displays information about reservoirs within a user-defined radius based on device or user-provided GPS coordinates.
- Implemented basic filtering features and displayed data using an interactive map. The map allows users to visualize reservoirs and access their attributes directly.
- The frontend was built using a fork of a previous web project created with **Hugo**, allowing us to quickly set up a responsive design with features such as light/dark mode auto-detection.
- The backend communicated with the Oracle database using a **REST API**, ensuring secure and efficient access to the data.

### Phase 3: Data Model Modification (not completed)
- This phase involved modifying the data model by adding new attributes, tables, and data as required to expand the system’s capabilities.
- Due to a lack of additional data available online, we were unable to complete this phase.

### Phase 4: Predictive Model Development
- Developed a basic linear regression model to predict water levels in reservoirs based on historical data from the past five years.
- The model aimed to provide predictions for the upcoming 12 months. While we managed to set up the regression framework, the limited time and data availability impacted the accuracy of the model.

### Phase 5: Model Optimization and Water Transfer Solution
- The goal of this phase was to optimize the predictive model and propose solutions for water transfers between reservoirs based on predictions.
- We optimized the model for performance; however, the implementation of determining which reservoirs should transfer water to others was not completed due to time constraints.

### Evaluation Criteria
The hackathon challenge valued the following aspects:
- **Data Accuracy**: The correctness and reliability of the data used and displayed.
- **Accessibility**: The usability and accessibility of the web application, including features for users with different needs.
- **Efficiency**: The performance and speed of the web application and database queries.
- **Prediction Quality**: The accuracy and reliability of the predictive model for future water levels.
- **Optimization**: The effectiveness of the proposed water transfer solutions and their implementation in the system.

Despite the limited time, we reached the finals, securing second place in the **Accessibility** category.

## Development Process
The team followed a collaborative approach using agile principles, mainly inspired by Scrum methodology. Given the short development time and our limited experience in web development and dynamic elements like interactive maps, the project was challenging yet rewarding.

- **Frontend**: Built using HTML, CSS, and JavaScript on top of a forked Hugo-based web project to save time and ensure responsiveness.
- **Backend**: The web application interacts directly with the Oracle database hosted on OCI through a REST API, retrieving and displaying relevant information based on user input.
- **Map Integration**: An interactive map was implemented to show reservoir locations and allow radius-based filtering.
- **Accessibility**: Various modes of accessibility were integrated, including color contrast adjustments, to make the interface user-friendly for diverse audiences.

## Areas for Improvement
While we successfully completed phases 1, 2, 4, and 5, the following areas present opportunities for improvement:
- **Predictive Model**: Finding additional data sources to improve the accuracy and robustness of the predictive model for reservoir levels.
- **Security Enhancements**: Implementing stronger security measures, such as protections against web scraping, API security, and securing the database access layers to safeguard sensitive data.
- **Interactive Map Features**: Enhancing the map for better user interaction and visualization.
- **Advanced Water Management Features**: Completing the implementation of the water transfer optimization system, including the identification of optimal reservoirs for water transfer.

## Website and more
To explore our project:
- Visit [our web application](https://dajer.netlify.app/es/) to see the interactive map and features.

### How to Use the Web Application
1. Navigate to [the map page](https://dajer.netlify.app/es/map/).
2. Enter your location and the radius within which you want to search for reservoirs.
3. The map will display all reservoirs within that radius, showing detailed information about each, including official government reports.
4. Click on a specific reservoir to view monthly predictions for water levels from today up to 12 months ahead.
5. For accessibility options, visit the "Accessibility" tab where you can:
   - Enable a **read-aloud mode** for page content.
   - Adjust font size with options to **increase** or **decrease** text size.
   - Switch between **high contrast** and **vintage** modes for the entire site.

## Team Members
- **David Muñoz del Valle**:
  - Attempted to set up the server on Oracle Cloud using Apache.
  - Managed group coordination and designed the algorithm for location-based data retrieval.
- **Artur Vargas Carrión**:
  - Conducted data analysis for the linear regression model and managed Oracle database integration and setup.
- **Juan Manuel Valenzuela González**:
  - Led the Oracle database setup and maintenance.
  - Developed the interactive map feature and assisted in implementing accessibility features on the website.
- **Eduardo González Bautista** (Team Lead 1):
  - Oversaw and actively contributed to the Oracle database setup, ensuring that the data was structured and usable for analysis and visualization.
  - Contributed to the development of the linear regression model.
  - Coordinated with the team to manage project deadlines and technical decisions.
- **Rubén Oliva Zamora** (Team Lead 2):
  - Planned the project phases and structured tasks according to the timeline.
  - Developed the frontend using the Hugo framework, ensuring responsiveness and accessibility.

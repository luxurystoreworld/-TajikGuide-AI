# TajikGuide AI Database Structure

## Places

- id
- name
- name_ru
- name_tj
- category
- region
- city
- description
- latitude
- longitude
- rating
- images

## Hotels

- id
- name
- city
- address
- phone
- website
- rating
- price_per_night

## Restaurants

- id
- name
- city
- cuisine
- address
- phone
- rating

## Tour Guides

- id
- full_name
- languages
- city
- experience
- rating
- phone

## Users

- id
- first_name
- last_name
- email
- password
- country
- language

## Trips

- id
- user_id
- place_id
- date
- status

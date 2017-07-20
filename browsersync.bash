#!/bin/bash
# Comentarios

browser-sync start --proxy "http://localhost:8000" --files "**/templates/**/*.html, static/css/*, static/js/*" 
exec bash



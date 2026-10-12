# README.md

This repository contains the data and code used to calculate the fuel cost for a single journey in NimbleBit's Pocket Planes.
The cost from flying between airports increases with distance and with the type of plane used but the calculation underlying this isn't obvious from the game.

The analysis uses 60 observations taken from the app across a range of distances and class 1, 2, and 3 aircraft.
The code, written in python, applies correlation, then regression analysis to test different possibilities and then to derive a model that predicts fuel costs given a specific aircraft speed, weight, and the distance flown.
The model is not perfect but has an average error of 0.32% and across the 60 observations has a max error of 3.6%. It seems to be slightly less accurate with certain upgraded aircraft, although it's unclear why.

The analysis is written in fuel_calc.qmd and can be run after cloning the repository, it relies on functions in pocket_planes_utils.py and uses airport location and trip data in data/.
Each time the .qmd is rendered additional analysis results are written to fuel_cost_model_results.txt.

If you're interested in improving the model feel free to submit the fuel cost that Pocket Planes shows for an (empty) trip between two locations, along with the aircraft's exact speed and weight.
In the future I hope to be able to put the model into a streamlit app which anyone can use to predict fuel costs and see how well the model works for themselves.
Feel free to contact me with any questions or suggestions you may have and please support the game's developers, [Nimblebit](https://nimblebit.com).


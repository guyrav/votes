import numpy as np


threshold = 0.325


def calculate_seats_and_indicators_simple(votes, num_seats=120):
    total_votes = sum(votes)
    seats = (votes * num_seats / total_votes).astype(int)
    indicators = np.zeros(len(votes), dtype=float)
    for i in range(sum(seats), num_seats):
        indicators = votes / (seats + 1)
        seats[np.argmax(indicators)] += 1
    return seats, indicators


def calculate_seats_and_indicators(votes, deals, num_seats=120):
    total_votes = sum(votes)
    votes[votes / total_votes < threshold] = 0
    votes_by_deal = [np.array([votes(i) for i in deal]) for deal in deals]
    seats_by_deal, indicators_by_deal = calculate_seats_and_indicators_simple(
        np.array(map(sum, votes_by_deal)), num_seats
    )
    seats = np.zeros(len(votes), dtype=int)
    indicators = np.zeros(len(votes), dtype=float)
    for deal, votes_in_deal, seats_in_deal in zip(deals, votes_by_deal, seats_by_deal):
        seats_by_party, indicators_by_party = calculate_seats_and_indicators_simple(
            votes_in_deal, seats_in_deal
        )
        for ind_party, party_seats, party_indicator in zip(deal, seats_by_party, indicators_by_party):
            seats[ind_party] = party_seats
            indicators[ind_party] = party_indicator

    return seats, indicators, seats_by_deal, indicators_by_deal

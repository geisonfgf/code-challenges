"""
Problem Statement

Time is running out. You have a final match to play as a counter terrorist.
You have N players each having a distinct ID from 1 to N. You have to choose
some players on your team from these N players such that no two chosen players
have consecutive numbers (as they tend to kill each other).
Also you definitely have to choose some K players whose numbers are given.
They are the snipers. Find the maximum number of players that you can choose.

Input Format

The first line contains 2 space-separated integers, N and K,
where N is the total number of players and K is the number of players that
have to be definitely in the team (the snipers). 
The second line contains K space-separated integers that are the IDs of the
snipers.

NOTE: There are no two snipers with consecutive numbers.

Constraints 
2 <= N <= 2x10^6 
1 <= K <= N/2 
1 <= ID of each sniper <= N

Output Format
You need to print the maximum number of players that you can have in your team.

Sample Input
8 2
6 2

Sample Output
4

Explanation

There are 8 players in total, among which you have to definitely choose
players with ID 2 and 6. 
To maximize the number of players in the team, you will choose the
players with IDs 4 and 8, so that you will have a total of 4 players.

Camper: A player in a professional team dedicated to using the AWP
sniper rifle.

Python SOLUTION

N, K = [int(x) for x in raw_input().strip().split(' ')]
a = sorted([int(x) for x in raw_input().strip().split(' ')])
ans = K

for i in xrange(1, K):
    ans += (a[i] - a[i - 1] - 2) / 2

if (a[0] > 2):
    ans += (a[0] - 1) / 2

if (a[K - 1] < N - 1):
    ans += (N + 1 - a[K - 1] - 1) / 2

print ans
"""

import unittest
import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Team(object):

    def __init__(self, _total_number_of_players,
                 _number_of_snippers, _snippers):
        self.total_number_of_players = _total_number_of_players
        self.number_of_players_selected = 0
        self.players = range(1, _total_number_of_players + 1)
        self.left_players = None
        self.not_seletable_players = None
        self.players_selected = None
        self.players_counted = []
        self.snippers = None
        if _snippers is not None:
            self.snippers = sorted(_snippers)
            self.__set_not_selectable_players()
            self.left_players = sorted(list(
                set(self.players) - set(self.not_seletable_players)))
            self.players_selected = sorted(list(
                set(self.snippers + self.left_players)))
            self.__calc_number_of_players_selected1()

    def __set_not_selectable_players(self):
        not_seletable_players = []
        for player in sorted(self.snippers):
            if player - 1 >= 1:
                not_seletable_players.append(player - 1)
            not_seletable_players.append(player)
            if player + 1 <= self.total_number_of_players:
                not_seletable_players.append(player + 1)
        self.not_seletable_players = sorted(not_seletable_players)

    def __calc_number_of_players_selected(self):
        for index in range(len(self.players_selected)):
            if index == 0:
                self.number_of_players_selected += 1
                self.players_counted.append(self.players_selected[index])
            elif index > 0 and self.players_selected[index - 1] % 2 == 0 and \
                    self.players_selected[index] % 2 == 0:
                if self.players_selected[index] % 2 == 0:
                    self.number_of_players_selected += 1
                    self.players_counted.append(self.players_selected[index])
            elif index > 0 and self.players_selected[0] % 2 == 1 and \
                    self.players_selected[index] % 2 == 1:
                if self.players_selected[index] % 2 == 1:
                    self.number_of_players_selected += 1
                    self.players_counted.append(self.players_selected[index])
            elif index > 0 and self.players_selected[index - 1] + 1 < self.players_selected[index]:
                self.number_of_players_selected += 1
                self.players_counted.append(self.players_selected[index])

    def __repr__(self):
        return ("{\n  players: %s"
                "\n  not_seletable_players: %s"
                "\n  left_players: %s"
                "\n  snippers: %s"
                "\n  players_selected: %s"
                "\n  players_counted: %s"
                "\n  number_of_players_selected: %s"
                "\n}") % (self.players,
                          self.not_seletable_players,
                          self.left_players,
                          self.snippers,
                          self.players_selected,
                          self.players_counted,
                          self.number_of_players_selected)


class CamperTest(unittest.TestCase):

    def testTeamWith8players2Snippers2_6(self):
        team = Team(8, 2, [2, 6])
        logger = logging.getLogger('TestTeamWith8players2Snippers2_6')
        logger.debug(team)
        self.assertEqual(
            team.number_of_players_selected, 4,
            "Incorrect Answer: {}".format(team.number_of_players_selected))

    def testTeamWith8players2Snippers1_6(self):
        team = Team(8, 2, [1, 6])
        logger = logging.getLogger('TestTeamWith8players2Snippers1_6')
        logger.debug(team)
        self.assertEqual(
            team.number_of_players_selected, 4,
            "Incorrect Answer: {}".format(team.number_of_players_selected))

    def testTeamWith8players2Snippers6_8(self):
        team = Team(8, 2, [6, 8])
        logger = logging.getLogger('TestTeamWith8players2Snippers6_8')
        logger.debug(team)
        self.assertEqual(
            team.number_of_players_selected, 4,
            "Incorrect Answer: {}".format(team.number_of_players_selected))

    def testTeamWith3players1Snippers1(self):
        team = Team(3, 1, [1])
        logger = logging.getLogger('TestTeamWith3players1Snippers1')
        logger.debug(team)
        self.assertEqual(
            team.number_of_players_selected, 2,
            "Incorrect Answer: {}".format(team.number_of_players_selected))

    def testTeamWith3players1Snippers2(self):
        team = Team(3, 1, [2])
        logger = logging.getLogger('TestTeamWith3players1Snippers2')
        logger.debug(team)
        self.assertEqual(
            team.number_of_players_selected, 1,
            "Incorrect Answer: {}".format(team.number_of_players_selected))

    def testTeamWith4players2Snippers2_4(self):
        team = Team(4, 2, [2,4])
        logger = logging.getLogger('TestTeamWith4players2Snippers2_4')
        logger.debug(team)
        self.assertEqual(
            team.number_of_players_selected, 2,
            "Incorrect Answer: {}".format(team.number_of_players_selected))

    def testTeamWith5players1Snippers3(self):
        team = Team(5, 1, [3])
        logger = logging.getLogger('TestTeamWith5players1Snippers3')
        logger.debug(team)
        self.assertEqual(
            team.number_of_players_selected, 3,
            "Incorrect Answer: {}".format(team.number_of_players_selected))

    def testTeamWith2players1Snippers1(self):
        team = Team(2, 1, [1])
        logger = logging.getLogger('TestTeamWith2players1Snippers1')
        logger.debug(team)
        self.assertEqual(
            team.number_of_players_selected, 1,
            "Incorrect Answer: {}".format(team.number_of_players_selected))

    def testTeamWith1000players15Snippers(self):
        team = Team(1000, 15, [936,693,92,854,622,453,512,541,190,763,302,587,250,402,585])
        logger = logging.getLogger('TestTeamWith2players1Snippers1')
        logger.debug(team)
        self.assertEqual(
            team.number_of_players_selected, 497,
            "Incorrect Answer: {}".format(team.number_of_players_selected))

if __name__ == '__main__':
    unittest.main()
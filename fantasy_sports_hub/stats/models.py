from django.db import models
from django.core.validators import MaxValueValidator
from teams.models import NflTeam
from standings.models import NflStanding
from schedule.models import NflGame
from django.core.validators import MaxValueValidator, MinValueValidator


class NflTeamRegularSeasonRecord(models.Model):
    season_year = models.PositiveIntegerField(blank=True, null=True)
    season_type = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    # Get team id filtering by team city/name
    team_id = models.ForeignKey(
        NflTeam, on_delete=models.CASCADE, related_name="id_team", blank=True, null=True)
    # Get standing id filtering by team city/name, year, and season type
    standing_id = models.ForeignKey(
        NflStanding, on_delete=models.CASCADE, related_name="standing_id", blank=True, null=True)


class NflGameStatsFinal(models.Model):
    season_year = models.PositiveIntegerField(blank=True, null=True)
    season_type = models.CharField(max_length=50, default="")
    home_team_id = models.ForeignKey(
        NflTeam, on_delete=models.CASCADE, related_name="home_team_id", blank=True, null=True)
    away_team_id = models.ForeignKey(
        NflTeam, on_delete=models.CASCADE, related_name="away_team_id", blank=True, null=True)
    game_id = models.ForeignKey(
        NflGame, on_delete=models.CASCADE, related_name="game", blank=True, null=True)
    home_team_rushing_attempts_count = models.PositiveIntegerField(default=0)
    home_team_total_rushing_yards = models.PositiveIntegerField(default=0)
    home_team_avg_yards_per_rush = models.FloatField(default=0.0)
#     home_team_points = models.PositiveSmallIntegerField(default=0)
#     away_team_points = models.PositiveSmallIntegerField(default=0)
#     home_team_quarter_1_points = models.PositiveSmallIntegerField(default=0)
#     away_team_quarter_1_points = models.PositiveSmallIntegerField(default=0)
#     home_team_quarter_2_points = models.PositiveSmallIntegerField(default=0)
#     away_team_quarter_2_points = models.PositiveSmallIntegerField(default=0)
#     home_team_quarter_3_points = models.PositiveSmallIntegerField(default=0)
#     away_team_quarter_3_points = models.PositiveSmallIntegerField(default=0)
#     home_team_quarter_4_points = models.PositiveSmallIntegerField(default=0)
#     away_team_quarter_4_points = models.PositiveSmallIntegerField(default=0)


class NflTeamRegularSeasonStats(models.Model):
    season_year = models.PositiveIntegerField(blank=True, null=True)
    season_type = models.CharField(max_length=50, default="")
    team_id = models.ForeignKey(
        NflTeam, on_delete=models.CASCADE, related_name="team_id", blank=True, null=True)
    standing_id = models.ForeignKey(
        NflStanding, on_delete=models.CASCADE, related_name="standing", blank=True, null=True)
    games_played_count = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(16)])
    # Touchdown stats
    total_touchdown_count = models.PositiveIntegerField(default=0)
    passing_touchdown_count = models.PositiveIntegerField(default=0)
    rushing_touchdown_count = models.PositiveIntegerField(default=0)
    total_return_touchdown_count = models.PositiveIntegerField(default=0)
    kick_return_touchdown_count = models.PositiveIntegerField(default=0)
    punt_return_touchdown_count = models.PositiveIntegerField(default=0)
    interception_return_touchdown_count = models.PositiveIntegerField(
        default=0)
    fumble_return_touchdown_count = models.PositiveIntegerField(default=0)
    # Rushing stats
    rushing_attempts_count = models.PositiveIntegerField(default=0)
    rushing_total_yards = models.PositiveIntegerField(default=0)
    rushing_avg_yards_per_rush = models.FloatField(default=0.0)
    rushing_touchdown_count = models.PositiveIntegerField(default=0)
    rusing_redzone_attempts_count = models.PositiveIntegerField(default=0)
    rusing_longest_rush = models.PositiveIntegerField(default=0)
    rusing_longest_touchdown = models.PositiveIntegerField(default=0)
    rusing_yards_after_contact = models.PositiveIntegerField(default=0)
    rusing_broken_tackles_count = models.PositiveIntegerField(default=0)
    # Receiving stats
    receiving_targets_count = models.PositiveIntegerField(default=0)
    receiving_receptions_count = models.PositiveIntegerField(default=0)
    receiving_avg_yards = models.FloatField(default=0.0)
    receiving_total_yards = models.PositiveIntegerField(default=0)
    receiving_touchdown_count = models.PositiveIntegerField(default=0)
    receiving_redzone_targets_count = models.PositiveIntegerField(default=0)
    receiving_longest_reception = models.PositiveIntegerField(default=0)
    receiving_longest_touchdown = models.PositiveIntegerField(default=0)
    receiving_yards_after_catch = models.PositiveIntegerField(default=0)
    receiving_broken_tackles_count = models.PositiveIntegerField(default=0)
    receiving_dropped_catchable_passes_count = models.PositiveIntegerField(
        default=0)
    receiving_catchable_passes_count = models.PositiveIntegerField(default=0)
    receiving_total_air_yards = models.PositiveIntegerField(default=0)
    # Passing stats
    passing_attempts_count = models.PositiveIntegerField(default=0)
    passing_total_yards = models.PositiveIntegerField(
        default=0)  # total/net yards
    passing_completions_count = models.PositiveIntegerField(default=0)
    passing_completion_percentage = models.FloatField(default=0.0)
    passing_touchdown_count = models.PositiveIntegerField(default=0)
    passing_redzone_attempts_count = models.PositiveIntegerField(default=0)
    passing_longest_pass = models.PositiveIntegerField(default=0)
    passing_longest_touchdown = models.PositiveIntegerField(default=0)
    passing_interceptions_count = models.PositiveIntegerField(default=0)
    passing_sacks_count = models.PositiveIntegerField(default=0)
    passing_dropped_passes_count = models.PositiveIntegerField(default=0)
    passing_throw_aways_count = models.PositiveIntegerField(default=0)
    passing_batted_passes_count = models.PositiveIntegerField(default=0)
    passing_hurried_count = models.PositiveIntegerField(default=0)
    passing_knockdowns_count = models.PositiveIntegerField(
        default=0)  # QB falls after throw
    passing_blitzes_faced_count = models.PositiveIntegerField(default=0)
    passing_poor_throws_count = models.PositiveIntegerField(default=0)
    # Penalty stats
    total_penalty_count = models.PositiveIntegerField(default=0)
    total_penalty_yards = models.PositiveIntegerField(default=0)
    # Efficiency stats
    goal_to_go_attempts = models.PositiveIntegerField(default=0)
    goal_to_go_successes = models.PositiveIntegerField(default=0)
    goal_to_go_percentage = models.FloatField(default=0.0)
    redzone_attempts = models.PositiveIntegerField(default=0)
    redzone_successes = models.PositiveIntegerField(default=0)
    redzone_percentage = models.FloatField(default=0.0)
    thirddown_attempts = models.PositiveIntegerField(default=0)
    thirddown_successes = models.PositiveIntegerField(default=0)
    thirddown_percentage = models.FloatField(default=0.0)
    fourthdown_attempts = models.PositiveIntegerField(default=0)
    fourthdown_successes = models.PositiveIntegerField(default=0)
    fourthdown_percentage = models.FloatField(default=0.0)
    # Defensive stats
    defense_tackles_count = models.PositiveIntegerField(default=0)
    defense_missed_tackle_count = models.PositiveIntegerField(default=0)
    defense_sacks_count = models.PositiveIntegerField(default=0)
    defense_interceptions_count = models.PositiveIntegerField(default=0)
    defense_forced_fumbles_count = models.PositiveIntegerField(default=0)
    defense_fumbles_recovery_count = models.PositiveIntegerField(default=0)
    defense_qb_hit_count = models.PositiveIntegerField(default=0)
    defense_safety_count = models.PositiveIntegerField(default=0)
    defense_batted_passes_count = models.PositiveIntegerField(default=0)
    defense_blitzes_count = models.PositiveIntegerField(default=0)
    defense_hurries_count = models.PositiveIntegerField(default=0)
    defense_knockdowns_count = models.PositiveIntegerField(default=0)
    # Opponent stats
    opponent_total_touchdown_count = models.PositiveIntegerField(default=0)
    opponent_passing_touchdown_count = models.PositiveIntegerField(default=0)
    opponent_rushing_touchdown_count = models.PositiveIntegerField(default=0)
    opponent_total_return_touchdown_count = models.PositiveIntegerField(
        default=0)
    opponent_kick_return_touchdown_count = models.PositiveIntegerField(
        default=0)
    opponent_punt_return_touchdown_count = models.PositiveIntegerField(
        default=0)
    opponent_interception_return_touchdown_count = models.PositiveIntegerField(
        default=0)
    opponent_fumble_return_touchdown_count = models.PositiveIntegerField(
        default=0)
    opponent_rushing_yards = models.PositiveIntegerField(default=0)
    opponent_passing_yards = models.PositiveIntegerField(default=0)

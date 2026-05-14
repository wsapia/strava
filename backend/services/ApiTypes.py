from enum import StrEnum
from dataclasses import dataclass


class ActivityType(StrEnum):
    ALPINESKI: "AlpineSki"
    BACKCOUNTRYSKI: "BackcountrySki"
    CANOEING: "Canoeing"
    CROSSFIT: "Crossfit"
    EBIKERIDE: "EBikeRide"
    ELLIPTICAL: "Elliptical"
    GOLF: "Golf"
    HANDCYCLE: "Handcycle"
    HIKE: "Hike"
    ICESKATE: "IceSkate"
    INLINESKATE: "InlineSkate"
    KAYAKING: "Kayaking"
    KITESURF: "Kitesurf"
    NORDICSKI: "NordicSki"
    RIDE: "Ride"
    ROCKCLIMBING: "RockClimbing"
    ROLLERSKI: "RollerSki"
    ROWING: "Rowing"
    RUN: "Run"
    SAIL: "Sail"
    SKATEBOARD: "Skateboard"
    SNOWBOARD: "Snowboard"
    SNOWSHOE: "Snowshoe"
    SOCCER: "Soccer"
    STAIRSTEPPER: "StairStepper"
    STANDUPPADDLING: "StandUpPaddling"
    SURFING: "Surfing"
    SWIM: "Swim"
    VELOMOBILE: "Velomobile"
    VIRTUALRIDE: "VirtualRide"
    VIRTUALRUN: "VirtualRun"
    WALK: "Walk"
    WEIGHTTRAINING: "WeightTraining"
    WHEELCHAIR: "Wheelchair"
    WINDSURF: "Windsurf"
    WORKOUT: "Workout"
    YOGA: "Yoga"


class SportType(StrEnum):
    ALPINESKI: "AlpineSki"
    BACKCOUNTRYSKI: "BackcountrySki"
    BADMINTON: "Badminton"
    BASKETBALL: "Basketball"
    CANOEING: "Canoeing"
    CRICKET: "Cricket"
    CROSSFIT: "Crossfit"
    DANCE: "Dance"
    EBIKERIDE: "EBikeRide"
    ELLIPTICAL: "Elliptical"
    EMOUNTAINBIKERIDE: "EMountainBikeRide"
    GOLF: "Golf"
    GRAVELRIDE: "GravelRide"
    HANDCYCLE: "Handcycle"
    HIGHINTENSITYINTERVALTRAINING: "HighIntensityIntervalTraining"
    HIKE: "Hike"
    ICESKATE: "IceSkate"
    INLINESKATE: "InlineSkate"
    KAYAKING: "Kayaking"
    KITESURF: "Kitesurf"
    MOUNTAINBIKERIDE: "MountainBikeRide"
    NORDICSKI: "NordicSki"
    PADEL: "Padel"
    PHYSICALTHERAPY: "PhysicalTherapy"
    PICKLEBALL: "Pickleball"
    PILATES: "Pilates"
    RACQUETBALL: "Racquetball"
    RIDE: "Ride"
    ROCKCLIMBING: "RockClimbing"
    ROLLERSKI: "RollerSki"
    ROWING: "Rowing"
    RUN: "Run"
    SAIL: "Sail"
    SKATEBOARD: "Skateboard"
    SNOWBOARD: "Snowboard"
    SNOWSHOE: "Snowshoe"
    SOCCER: "Soccer"
    SQUASH: "Squash"
    STAIRSTEPPER: "StairStepper"
    STANDUPPADDLING: "StandUpPaddling"
    SURFING: "Surfing"
    SWIM: "Swim"
    TABLETENNIS: "TableTennis"
    TENNIS: "Tennis"
    TRAILRUN: "TrailRun"
    VELOMOBILE: "Velomobile"
    VIRTUALRIDE: "VirtualRide"
    VIRTUALROW: "VirtualRow"
    VIRTUALRUN: "VirtualRun"
    VOLLEYBALL: "Volleyball"
    WALK: "Walk"
    WEIGHTTRAINING: "WeightTraining"
    WHEELCHAIR: "Wheelchair"
    WINDSURF: "Windsurf"
    WORKOUT: "Workout"
    YOGA: "Yoga"


@dataclass
class ActivityTotal:
    count: int
    distance: float
    moving_time: int
    elapsed_time: int
    elevation_gain: float
    achievement_count: int


@dataclass
class ActivityStats:
    biggest_ride_distance: float
    biggest_climb_elevation_gain: float
    recent_ride_totals: ActivityTotal
    recent_run_totals: ActivityTotal
    recent_swim_totals: ActivityTotal
    ytd_ride_totals: ActivityTotal
    ytd_run_totals: ActivityTotal
    ytd_swim_totals: ActivityTotal
    all_ride_totals: ActivityTotal
    all_run_totals: ActivityTotal
    all_swim_totals: ActivityTotal


@dataclass
class MetaActivity:
    id: int


@dataclass
class MetaAthlete:
    id: int


@dataclass
class MetaClub:
    id: int
    resource_state: int
    name: str


@dataclass
class PolylineMap:
    id: str
    polyline: str
    summary_polyline: str


@dataclass
class BaseStream:
    original_size: int
    resolution: str
    series_type: str


@dataclass
class ClubAthlete:
    resource_state: int
    firstname: str
    lastname: str
    member: str
    admin: bool
    owner: bool


@dataclass
class Error:
    code: str
    field: str
    resource: str


@dataclass
class Fault:
    errors: Error
    message: str


@dataclass
class PhotosSummaryPrimary:
    id: int
    source: int
    unique_id: str
    urls: str


@dataclass
class Split:
    average_speed: float
    distance: float
    elapsed_time: int
    elevation_difference: float
    pace_zone: int
    moving_time: int
    split: int


@dataclass
class SummaryGear:
    id: str
    resource_state: int
    primary: bool
    name: str
    distance: float


@dataclass
class SummaryPRSegmentEffort:
    pr_activity_id: int
    pr_elapsed_time: int
    pr_date: str
    effort_count: int


@dataclass
class SummarySegmentEffort:
    id: int
    activity_id: int
    elapsed_time: int
    start_date: str
    start_date_local: str
    distance: float
    is_kom: bool


@dataclass
class Upload:
    id: int
    id_str: str
    external_id: str
    error: str
    status: str
    activity_id: int


@dataclass
class ZoneRange:
    min: int
    max: int


@dataclass
class HeartRateZoneRanges:
    custom_zones: bool
    zones: list[ZoneRange]


@dataclass
class PowerZoneRanges:
    zones: list[ZoneRange]


@dataclass
class Zones:
    heart_rate: HeartRateZoneRanges
    power: PowerZoneRanges


@dataclass
class AltitudeStream:
    original_size: int
    resolution: str
    series_type: str
    data: float


@dataclass
class CadenceStream:
    original_size: int
    resolution: str
    series_type: str
    data: int


@dataclass
class DetailedGear:
    id: str
    resource_state: int
    primary: bool
    name: str
    distance: float
    brand_name: str
    model_name: str
    frame_type: int
    description: str


@dataclass
class DistanceStream:
    original_size: int
    resolution: str
    series_type: str
    data: float


@dataclass
class HeartrateStream:
    original_size: int
    resolution: str
    series_type: str
    data: int


@dataclass
class MovingStream:
    original_size: int
    resolution: str
    series_type: str
    data: bool


@dataclass
class PowerStream:
    original_size: int
    resolution: str
    series_type: str
    data: int


@dataclass
class SmoothGradeStream:
    original_size: int
    resolution: str
    series_type: str
    data: float


@dataclass
class SmoothVelocityStream:
    original_size: int
    resolution: str
    series_type: str
    data: float


@dataclass
class SummaryAthlete:
    id: int
    resource_state: int
    firstname: str
    lastname: str
    profile_medium: str
    profile: str
    city: str
    state: str
    country: str
    sex: str
    premium: bool
    summit: bool
    created_at: str
    updated_at: str


@dataclass
class TemperatureStream:
    original_size: int
    resolution: str
    series_type: str
    data: int


@dataclass
class TimeStream:
    original_size: int
    resolution: str
    series_type: str
    data: int


@dataclass
class TimedZoneRange:
    min: int
    max: int
    time: int


@dataclass
class TimedZoneDistribution:
    timed_zone_ranges: list[TimedZoneRange]


@dataclass
class ActivityZone:
    score: int
    distribution_buckets: TimedZoneDistribution
    type: str
    sensor_based: bool
    points: int
    custom_zones: bool
    max: int


@dataclass
class ClubActivity:
    athlete: MetaAthlete
    name: str
    distance: float
    moving_time: int
    elapsed_time: int
    total_elevation_gain: float
    type: ActivityType
    sport_type: SportType
    workout_type: int


@dataclass
class Comment:
    id: int
    activity_id: int
    text: str
    athlete: SummaryAthlete
    created_at: str


class LatLng:
    lat: float
    lng: float


@dataclass
class ExplorerSegment:
    id: int
    name: str
    climb_category: int
    climb_category_desc: str
    avg_grade: float
    start_latlng: LatLng
    end_latlng: LatLng
    elev_difference: float
    distance: float
    points: str


@dataclass
class ExplorerResponse:
    segments: ExplorerSegment


@dataclass
class HeartRateZoneRanges:
    custom_zones: bool
    zones: list[ZoneRange]


@dataclass
class Lap:
    id: int
    activity: MetaActivity
    athlete: MetaAthlete
    average_cadence: float
    average_speed: float
    distance: float
    elapsed_time: int
    start_index: int
    end_index: int
    lap_index: int
    max_speed: float
    moving_time: int
    name: str
    pace_zone: int
    split: int
    start_date: str
    start_date_local: str
    total_elevation_gain: float


@dataclass
class PhotosSummary:
    count: int
    primary: PhotosSummaryPrimary


@dataclass
class PowerZoneRanges:
    zones: list[ZoneRange]


@dataclass
class SummarySegment:
    id: int
    name: str
    activity_type: str
    distance: float
    average_grade: float
    maximum_grade: float
    elevation_high: float
    elevation_low: float
    start_latlng: LatLng
    end_latlng: LatLng
    climb_category: int
    city: str
    state: str
    country: str
    private: bool
    athlete_pr_effort: SummaryPRSegmentEffort
    athlete_segment_stats: SummarySegmentEffort


@dataclass
class Waypoint:
    latlng: LatLng
    target_latlng: LatLng
    categories: str
    title: str
    description: str
    distance_into_route: float


@dataclass
class Route:
    athlete: SummaryAthlete
    description: str
    distance: float
    elevation_gain: float
    id: int
    id_str: str
    map: PolylineMap
    name: str
    private: bool
    starred: bool
    timestamp: int
    type: int
    sub_type: int
    created_at: str
    updated_at: str
    estimated_moving_time: int
    segments: SummarySegment
    waypoints: Waypoint


@dataclass
class LatLngStream:
    original_size: int
    resolution: str
    series_type: str
    data: LatLng


@dataclass
class StreamSet:
    time: TimeStream
    distance: DistanceStream
    latlng: LatLngStream
    altitude: AltitudeStream
    velocity_smooth: SmoothVelocityStream
    heartrate: HeartrateStream
    cadence: CadenceStream
    watts: PowerStream
    temp: TemperatureStream
    moving: MovingStream
    grade_smooth: SmoothGradeStream


@dataclass
class UpdatableActivity:
    commute: bool
    trainer: bool
    hide_from_home: bool
    description: str
    name: str
    type: ActivityType
    sport_type: SportType
    gear_id: str


@dataclass
class DetailedSegment:
    id: int
    name: str
    activity_type: str
    distance: float
    average_grade: float
    maximum_grade: float
    elevation_high: float
    elevation_low: float
    start_latlng: LatLng
    end_latlng: LatLng
    climb_category: int
    city: str
    state: str
    country: str
    private: bool
    athlete_pr_effort: SummaryPRSegmentEffort
    athlete_segment_stats: SummarySegmentEffort
    created_at: str
    updated_at: str
    total_elevation_gain: float
    map: PolylineMap
    effort_count: int
    athlete_count: int
    hazardous: bool
    star_count: int


@dataclass
class DetailedSegmentEffort:
    id: int
    activity_id: int
    elapsed_time: int
    start_date: str
    start_date_local: str
    distance: float
    is_kom: bool
    name: str
    activity: MetaActivity
    athlete: MetaAthlete
    moving_time: int
    start_index: int
    end_index: int
    average_cadence: float
    average_watts: float
    device_watts: bool
    average_heartrate: float
    max_heartrate: float
    segment: SummarySegment
    kom_rank: int
    pr_rank: int
    hidden: bool


@dataclass
class SummaryActivity:
    id: int
    external_id: str
    upload_id: int
    athlete: MetaAthlete
    name: str
    distance: float
    moving_time: int
    elapsed_time: int
    total_elevation_gain: float
    elev_high: float
    elev_low: float
    type: ActivityType
    sport_type: SportType
    start_date: str
    start_date_local: str
    timezone: str
    start_latlng: LatLng
    end_latlng: LatLng
    achievement_count: int
    kudos_count: int
    comment_count: int
    athlete_count: int
    photo_count: int
    total_photo_count: int
    map: PolylineMap
    device_name: str
    trainer: bool
    commute: bool
    manual: bool
    private: bool
    flagged: bool
    workout_type: int
    upload_id_str: str
    average_speed: float
    max_speed: float
    has_kudoed: bool
    hide_from_home: bool
    gear_id: str
    kilojoules: float
    average_watts: float
    device_watts: bool
    max_watts: int
    weighted_average_watts: int


@dataclass
class SummaryClub:
    id: int
    resource_state: int
    name: str
    profile_medium: str
    cover_photo: str
    cover_photo_small: str
    sport_type: str
    activity_types: ActivityType
    city: str
    state: str
    country: str
    private: bool
    member_count: int
    featured: bool
    verified: bool
    url: str


@dataclass
class DetailedActivity:
    id: int
    external_id: str
    upload_id: int
    athlete: MetaAthlete
    name: str
    distance: float
    moving_time: int
    elapsed_time: int
    total_elevation_gain: float
    elev_high: float
    elev_low: float
    type: ActivityType
    sport_type: SportType
    start_date: str
    start_date_local: str
    timezone: str
    start_latlng: LatLng
    end_latlng: LatLng
    achievement_count: int
    kudos_count: int
    comment_count: int
    athlete_count: int
    photo_count: int
    total_photo_count: int
    map: PolylineMap
    device_name: str
    trainer: bool
    commute: bool
    manual: bool
    private: bool
    flagged: bool
    workout_type: int
    upload_id_str: str
    average_speed: float
    max_speed: float
    has_kudoed: bool
    hide_from_home: bool
    gear_id: str
    kilojoules: float
    average_watts: float
    device_watts: bool
    max_watts: int
    weighted_average_watts: int
    description: str
    photos: PhotosSummary
    gear: SummaryGear
    calories: float
    segment_efforts: DetailedSegmentEffort
    embed_token: str
    splits_metric: Split
    splits_standard: Split
    laps: Lap
    best_efforts: DetailedSegmentEffort


@dataclass
class DetailedAthlete:
    id: int
    resource_state: int
    firstname: str
    lastname: str
    profile_medium: str
    profile: str
    city: str
    state: str
    country: str
    sex: str
    premium: bool
    summit: bool
    created_at: str
    updated_at: str
    follower_count: int
    friend_count: int
    measurement_preference: str
    ftp: int
    weight: float
    clubs: SummaryClub
    bikes: SummaryGear
    shoes: SummaryGear


@dataclass
class DetailedClub:
    id: int
    resource_state: int
    name: str
    profile_medium: str
    cover_photo: str
    cover_photo_small: str
    sport_type: str
    activity_types: ActivityType
    city: str
    state: str
    country: str
    private: bool
    member_count: int
    featured: bool
    verified: bool
    url: str
    membership: str
    admin: bool
    owner: bool
    following_count: int

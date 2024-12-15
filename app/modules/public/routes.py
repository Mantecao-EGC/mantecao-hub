import logging

from flask import render_template, redirect, url_for
from flask_login import current_user

from app.modules.featuremodel.services import FeatureModelService
from app.modules.public import public_bp
from app.modules.dataset.services import DataSetService
from app.modules.profile.services import UserProfileService

logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
    logger.info("Access index")
    dataset_service = DataSetService()
    feature_model_service = FeatureModelService()

    # Statistics: total datasets and feature models
    datasets_counter = dataset_service.count_synchronized_datasets()
    feature_models_counter = feature_model_service.count_feature_models()

    # Statistics: total downloads
    total_dataset_downloads = dataset_service.total_dataset_downloads()
    total_feature_model_downloads = feature_model_service.total_feature_model_downloads()

    # Statistics: total views
    total_dataset_views = dataset_service.total_dataset_views()
    total_feature_model_views = feature_model_service.total_feature_model_views()

    return render_template(
        "public/index.html",
        datasets=dataset_service.latest_synchronized(),
        datasets_counter=datasets_counter,
        feature_models_counter=feature_models_counter,
        total_dataset_downloads=total_dataset_downloads,
        total_feature_model_downloads=total_feature_model_downloads,
        total_dataset_views=total_dataset_views,
        total_feature_model_views=total_feature_model_views
    )


@public_bp.route("/user/<int:user_id>")
def view_user_profile(user_id):
    logger.info(f"Access user profile: {user_id}")
    if current_user.is_authenticated and user_id == current_user.id:
        return redirect(url_for('profile.my_profile'))

    profile_service = UserProfileService()
    user_profile = profile_service.get_user_profile(user_id)
    if not user_profile:
        return render_template("errors/404.html"), 404

    dataset_service = DataSetService()
    user_datasets = dataset_service.get_datasets_by_user(user_id)

    return render_template(
        "profile/view_profile.html",
        user_profile=user_profile,
        user=user_profile.user,
        datasets=user_datasets,
        total_datasets=len(user_datasets)
    )

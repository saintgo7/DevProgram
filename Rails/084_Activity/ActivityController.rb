class ActivityController < ApplicationController
  before_action :set_activity, only: [:show, :edit, :update, :destroy]

  # GET /activity
  def index
    @activitys = Activity.all
    render json: @activitys
  end

  # GET /activity/1
  def show
    render json: @activity
  end

  # POST /activity
  def create
    @activity = Activity.new(activity_params)

    if @activity.save
      render json: @activity, status: :created
    else
      render json: @activity.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /activity/1
  def update
    if @activity.update(activity_params)
      render json: @activity
    else
      render json: @activity.errors, status: :unprocessable_entity
    end
  end

  # DELETE /activity/1
  def destroy
    @activity.destroy
    head :no_content
  end

  private

  def set_activity
    @activity = Activity.find(params[:id])
  end

  def activity_params
    params.require(:activity).permit(:name)
  end
end

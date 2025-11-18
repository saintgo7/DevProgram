class AnalyticsController < ApplicationController
  before_action :set_analytics, only: [:show, :edit, :update, :destroy]

  # GET /analytics
  def index
    @analyticss = Analytics.all
    render json: @analyticss
  end

  # GET /analytics/1
  def show
    render json: @analytics
  end

  # POST /analytics
  def create
    @analytics = Analytics.new(analytics_params)

    if @analytics.save
      render json: @analytics, status: :created
    else
      render json: @analytics.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /analytics/1
  def update
    if @analytics.update(analytics_params)
      render json: @analytics
    else
      render json: @analytics.errors, status: :unprocessable_entity
    end
  end

  # DELETE /analytics/1
  def destroy
    @analytics.destroy
    head :no_content
  end

  private

  def set_analytics
    @analytics = Analytics.find(params[:id])
  end

  def analytics_params
    params.require(:analytics).permit(:name)
  end
end

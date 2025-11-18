class TrackingController < ApplicationController
  before_action :set_tracking, only: [:show, :edit, :update, :destroy]

  # GET /tracking
  def index
    @trackings = Tracking.all
    render json: @trackings
  end

  # GET /tracking/1
  def show
    render json: @tracking
  end

  # POST /tracking
  def create
    @tracking = Tracking.new(tracking_params)

    if @tracking.save
      render json: @tracking, status: :created
    else
      render json: @tracking.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /tracking/1
  def update
    if @tracking.update(tracking_params)
      render json: @tracking
    else
      render json: @tracking.errors, status: :unprocessable_entity
    end
  end

  # DELETE /tracking/1
  def destroy
    @tracking.destroy
    head :no_content
  end

  private

  def set_tracking
    @tracking = Tracking.find(params[:id])
  end

  def tracking_params
    params.require(:tracking).permit(:name)
  end
end

class LocationController < ApplicationController
  before_action :set_location, only: [:show, :edit, :update, :destroy]

  # GET /location
  def index
    @locations = Location.all
    render json: @locations
  end

  # GET /location/1
  def show
    render json: @location
  end

  # POST /location
  def create
    @location = Location.new(location_params)

    if @location.save
      render json: @location, status: :created
    else
      render json: @location.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /location/1
  def update
    if @location.update(location_params)
      render json: @location
    else
      render json: @location.errors, status: :unprocessable_entity
    end
  end

  # DELETE /location/1
  def destroy
    @location.destroy
    head :no_content
  end

  private

  def set_location
    @location = Location.find(params[:id])
  end

  def location_params
    params.require(:location).permit(:name)
  end
end

class ZoneController < ApplicationController
  before_action :set_zone, only: [:show, :edit, :update, :destroy]

  # GET /zone
  def index
    @zones = Zone.all
    render json: @zones
  end

  # GET /zone/1
  def show
    render json: @zone
  end

  # POST /zone
  def create
    @zone = Zone.new(zone_params)

    if @zone.save
      render json: @zone, status: :created
    else
      render json: @zone.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /zone/1
  def update
    if @zone.update(zone_params)
      render json: @zone
    else
      render json: @zone.errors, status: :unprocessable_entity
    end
  end

  # DELETE /zone/1
  def destroy
    @zone.destroy
    head :no_content
  end

  private

  def set_zone
    @zone = Zone.find(params[:id])
  end

  def zone_params
    params.require(:zone).permit(:name)
  end
end

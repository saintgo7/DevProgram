class GeographyController < ApplicationController
  before_action :set_geography, only: [:show, :edit, :update, :destroy]

  # GET /geography
  def index
    @geographys = Geography.all
    render json: @geographys
  end

  # GET /geography/1
  def show
    render json: @geography
  end

  # POST /geography
  def create
    @geography = Geography.new(geography_params)

    if @geography.save
      render json: @geography, status: :created
    else
      render json: @geography.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /geography/1
  def update
    if @geography.update(geography_params)
      render json: @geography
    else
      render json: @geography.errors, status: :unprocessable_entity
    end
  end

  # DELETE /geography/1
  def destroy
    @geography.destroy
    head :no_content
  end

  private

  def set_geography
    @geography = Geography.find(params[:id])
  end

  def geography_params
    params.require(:geography).permit(:name)
  end
end

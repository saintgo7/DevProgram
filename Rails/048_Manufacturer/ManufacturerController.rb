class ManufacturerController < ApplicationController
  before_action :set_manufacturer, only: [:show, :edit, :update, :destroy]

  # GET /manufacturer
  def index
    @manufacturers = Manufacturer.all
    render json: @manufacturers
  end

  # GET /manufacturer/1
  def show
    render json: @manufacturer
  end

  # POST /manufacturer
  def create
    @manufacturer = Manufacturer.new(manufacturer_params)

    if @manufacturer.save
      render json: @manufacturer, status: :created
    else
      render json: @manufacturer.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /manufacturer/1
  def update
    if @manufacturer.update(manufacturer_params)
      render json: @manufacturer
    else
      render json: @manufacturer.errors, status: :unprocessable_entity
    end
  end

  # DELETE /manufacturer/1
  def destroy
    @manufacturer.destroy
    head :no_content
  end

  private

  def set_manufacturer
    @manufacturer = Manufacturer.find(params[:id])
  end

  def manufacturer_params
    params.require(:manufacturer).permit(:name)
  end
end

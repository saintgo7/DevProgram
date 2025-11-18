class ShipmentController < ApplicationController
  before_action :set_shipment, only: [:show, :edit, :update, :destroy]

  # GET /shipment
  def index
    @shipments = Shipment.all
    render json: @shipments
  end

  # GET /shipment/1
  def show
    render json: @shipment
  end

  # POST /shipment
  def create
    @shipment = Shipment.new(shipment_params)

    if @shipment.save
      render json: @shipment, status: :created
    else
      render json: @shipment.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /shipment/1
  def update
    if @shipment.update(shipment_params)
      render json: @shipment
    else
      render json: @shipment.errors, status: :unprocessable_entity
    end
  end

  # DELETE /shipment/1
  def destroy
    @shipment.destroy
    head :no_content
  end

  private

  def set_shipment
    @shipment = Shipment.find(params[:id])
  end

  def shipment_params
    params.require(:shipment).permit(:name)
  end
end

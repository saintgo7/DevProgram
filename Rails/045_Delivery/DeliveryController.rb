class DeliveryController < ApplicationController
  before_action :set_delivery, only: [:show, :edit, :update, :destroy]

  # GET /delivery
  def index
    @deliverys = Delivery.all
    render json: @deliverys
  end

  # GET /delivery/1
  def show
    render json: @delivery
  end

  # POST /delivery
  def create
    @delivery = Delivery.new(delivery_params)

    if @delivery.save
      render json: @delivery, status: :created
    else
      render json: @delivery.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /delivery/1
  def update
    if @delivery.update(delivery_params)
      render json: @delivery
    else
      render json: @delivery.errors, status: :unprocessable_entity
    end
  end

  # DELETE /delivery/1
  def destroy
    @delivery.destroy
    head :no_content
  end

  private

  def set_delivery
    @delivery = Delivery.find(params[:id])
  end

  def delivery_params
    params.require(:delivery).permit(:name)
  end
end

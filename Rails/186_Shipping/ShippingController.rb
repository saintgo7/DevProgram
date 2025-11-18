class ShippingController < ApplicationController
  before_action :set_shipping, only: [:show, :edit, :update, :destroy]

  # GET /shipping
  def index
    @shippings = Shipping.all
    render json: @shippings
  end

  # GET /shipping/1
  def show
    render json: @shipping
  end

  # POST /shipping
  def create
    @shipping = Shipping.new(shipping_params)

    if @shipping.save
      render json: @shipping, status: :created
    else
      render json: @shipping.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /shipping/1
  def update
    if @shipping.update(shipping_params)
      render json: @shipping
    else
      render json: @shipping.errors, status: :unprocessable_entity
    end
  end

  # DELETE /shipping/1
  def destroy
    @shipping.destroy
    head :no_content
  end

  private

  def set_shipping
    @shipping = Shipping.find(params[:id])
  end

  def shipping_params
    params.require(:shipping).permit(:name)
  end
end

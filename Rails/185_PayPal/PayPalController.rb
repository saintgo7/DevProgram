class PayPalController < ApplicationController
  before_action :set_paypal, only: [:show, :edit, :update, :destroy]

  # GET /paypal
  def index
    @paypals = PayPal.all
    render json: @paypals
  end

  # GET /paypal/1
  def show
    render json: @paypal
  end

  # POST /paypal
  def create
    @paypal = PayPal.new(paypal_params)

    if @paypal.save
      render json: @paypal, status: :created
    else
      render json: @paypal.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /paypal/1
  def update
    if @paypal.update(paypal_params)
      render json: @paypal
    else
      render json: @paypal.errors, status: :unprocessable_entity
    end
  end

  # DELETE /paypal/1
  def destroy
    @paypal.destroy
    head :no_content
  end

  private

  def set_paypal
    @paypal = PayPal.find(params[:id])
  end

  def paypal_params
    params.require(:paypal).permit(:name)
  end
end

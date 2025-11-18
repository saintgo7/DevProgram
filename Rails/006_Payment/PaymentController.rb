class PaymentController < ApplicationController
  before_action :set_payment, only: [:show, :edit, :update, :destroy]

  # GET /payment
  def index
    @payments = Payment.all
    render json: @payments
  end

  # GET /payment/1
  def show
    render json: @payment
  end

  # POST /payment
  def create
    @payment = Payment.new(payment_params)

    if @payment.save
      render json: @payment, status: :created
    else
      render json: @payment.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /payment/1
  def update
    if @payment.update(payment_params)
      render json: @payment
    else
      render json: @payment.errors, status: :unprocessable_entity
    end
  end

  # DELETE /payment/1
  def destroy
    @payment.destroy
    head :no_content
  end

  private

  def set_payment
    @payment = Payment.find(params[:id])
  end

  def payment_params
    params.require(:payment).permit(:name)
  end
end

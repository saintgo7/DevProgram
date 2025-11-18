class PaymentMethodController < ApplicationController
  before_action :set_paymentmethod, only: [:show, :edit, :update, :destroy]

  # GET /paymentmethod
  def index
    @paymentmethods = PaymentMethod.all
    render json: @paymentmethods
  end

  # GET /paymentmethod/1
  def show
    render json: @paymentmethod
  end

  # POST /paymentmethod
  def create
    @paymentmethod = PaymentMethod.new(paymentmethod_params)

    if @paymentmethod.save
      render json: @paymentmethod, status: :created
    else
      render json: @paymentmethod.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /paymentmethod/1
  def update
    if @paymentmethod.update(paymentmethod_params)
      render json: @paymentmethod
    else
      render json: @paymentmethod.errors, status: :unprocessable_entity
    end
  end

  # DELETE /paymentmethod/1
  def destroy
    @paymentmethod.destroy
    head :no_content
  end

  private

  def set_paymentmethod
    @paymentmethod = PaymentMethod.find(params[:id])
  end

  def paymentmethod_params
    params.require(:paymentmethod).permit(:name)
  end
end

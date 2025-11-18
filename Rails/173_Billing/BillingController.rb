class BillingController < ApplicationController
  before_action :set_billing, only: [:show, :edit, :update, :destroy]

  # GET /billing
  def index
    @billings = Billing.all
    render json: @billings
  end

  # GET /billing/1
  def show
    render json: @billing
  end

  # POST /billing
  def create
    @billing = Billing.new(billing_params)

    if @billing.save
      render json: @billing, status: :created
    else
      render json: @billing.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /billing/1
  def update
    if @billing.update(billing_params)
      render json: @billing
    else
      render json: @billing.errors, status: :unprocessable_entity
    end
  end

  # DELETE /billing/1
  def destroy
    @billing.destroy
    head :no_content
  end

  private

  def set_billing
    @billing = Billing.find(params[:id])
  end

  def billing_params
    params.require(:billing).permit(:name)
  end
end

class RefundController < ApplicationController
  before_action :set_refund, only: [:show, :edit, :update, :destroy]

  # GET /refund
  def index
    @refunds = Refund.all
    render json: @refunds
  end

  # GET /refund/1
  def show
    render json: @refund
  end

  # POST /refund
  def create
    @refund = Refund.new(refund_params)

    if @refund.save
      render json: @refund, status: :created
    else
      render json: @refund.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /refund/1
  def update
    if @refund.update(refund_params)
      render json: @refund
    else
      render json: @refund.errors, status: :unprocessable_entity
    end
  end

  # DELETE /refund/1
  def destroy
    @refund.destroy
    head :no_content
  end

  private

  def set_refund
    @refund = Refund.find(params[:id])
  end

  def refund_params
    params.require(:refund).permit(:name)
  end
end

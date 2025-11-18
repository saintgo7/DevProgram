class DiscountController < ApplicationController
  before_action :set_discount, only: [:show, :edit, :update, :destroy]

  # GET /discount
  def index
    @discounts = Discount.all
    render json: @discounts
  end

  # GET /discount/1
  def show
    render json: @discount
  end

  # POST /discount
  def create
    @discount = Discount.new(discount_params)

    if @discount.save
      render json: @discount, status: :created
    else
      render json: @discount.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /discount/1
  def update
    if @discount.update(discount_params)
      render json: @discount
    else
      render json: @discount.errors, status: :unprocessable_entity
    end
  end

  # DELETE /discount/1
  def destroy
    @discount.destroy
    head :no_content
  end

  private

  def set_discount
    @discount = Discount.find(params[:id])
  end

  def discount_params
    params.require(:discount).permit(:name)
  end
end

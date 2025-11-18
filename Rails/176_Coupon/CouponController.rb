class CouponController < ApplicationController
  before_action :set_coupon, only: [:show, :edit, :update, :destroy]

  # GET /coupon
  def index
    @coupons = Coupon.all
    render json: @coupons
  end

  # GET /coupon/1
  def show
    render json: @coupon
  end

  # POST /coupon
  def create
    @coupon = Coupon.new(coupon_params)

    if @coupon.save
      render json: @coupon, status: :created
    else
      render json: @coupon.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /coupon/1
  def update
    if @coupon.update(coupon_params)
      render json: @coupon
    else
      render json: @coupon.errors, status: :unprocessable_entity
    end
  end

  # DELETE /coupon/1
  def destroy
    @coupon.destroy
    head :no_content
  end

  private

  def set_coupon
    @coupon = Coupon.find(params[:id])
  end

  def coupon_params
    params.require(:coupon).permit(:name)
  end
end

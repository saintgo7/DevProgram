class PromotionController < ApplicationController
  before_action :set_promotion, only: [:show, :edit, :update, :destroy]

  # GET /promotion
  def index
    @promotions = Promotion.all
    render json: @promotions
  end

  # GET /promotion/1
  def show
    render json: @promotion
  end

  # POST /promotion
  def create
    @promotion = Promotion.new(promotion_params)

    if @promotion.save
      render json: @promotion, status: :created
    else
      render json: @promotion.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /promotion/1
  def update
    if @promotion.update(promotion_params)
      render json: @promotion
    else
      render json: @promotion.errors, status: :unprocessable_entity
    end
  end

  # DELETE /promotion/1
  def destroy
    @promotion.destroy
    head :no_content
  end

  private

  def set_promotion
    @promotion = Promotion.find(params[:id])
  end

  def promotion_params
    params.require(:promotion).permit(:name)
  end
end

class DealController < ApplicationController
  before_action :set_deal, only: [:show, :edit, :update, :destroy]

  # GET /deal
  def index
    @deals = Deal.all
    render json: @deals
  end

  # GET /deal/1
  def show
    render json: @deal
  end

  # POST /deal
  def create
    @deal = Deal.new(deal_params)

    if @deal.save
      render json: @deal, status: :created
    else
      render json: @deal.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /deal/1
  def update
    if @deal.update(deal_params)
      render json: @deal
    else
      render json: @deal.errors, status: :unprocessable_entity
    end
  end

  # DELETE /deal/1
  def destroy
    @deal.destroy
    head :no_content
  end

  private

  def set_deal
    @deal = Deal.find(params[:id])
  end

  def deal_params
    params.require(:deal).permit(:name)
  end
end

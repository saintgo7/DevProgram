class RetailerController < ApplicationController
  before_action :set_retailer, only: [:show, :edit, :update, :destroy]

  # GET /retailer
  def index
    @retailers = Retailer.all
    render json: @retailers
  end

  # GET /retailer/1
  def show
    render json: @retailer
  end

  # POST /retailer
  def create
    @retailer = Retailer.new(retailer_params)

    if @retailer.save
      render json: @retailer, status: :created
    else
      render json: @retailer.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /retailer/1
  def update
    if @retailer.update(retailer_params)
      render json: @retailer
    else
      render json: @retailer.errors, status: :unprocessable_entity
    end
  end

  # DELETE /retailer/1
  def destroy
    @retailer.destroy
    head :no_content
  end

  private

  def set_retailer
    @retailer = Retailer.find(params[:id])
  end

  def retailer_params
    params.require(:retailer).permit(:name)
  end
end

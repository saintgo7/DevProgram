class OfferController < ApplicationController
  before_action :set_offer, only: [:show, :edit, :update, :destroy]

  # GET /offer
  def index
    @offers = Offer.all
    render json: @offers
  end

  # GET /offer/1
  def show
    render json: @offer
  end

  # POST /offer
  def create
    @offer = Offer.new(offer_params)

    if @offer.save
      render json: @offer, status: :created
    else
      render json: @offer.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /offer/1
  def update
    if @offer.update(offer_params)
      render json: @offer
    else
      render json: @offer.errors, status: :unprocessable_entity
    end
  end

  # DELETE /offer/1
  def destroy
    @offer.destroy
    head :no_content
  end

  private

  def set_offer
    @offer = Offer.find(params[:id])
  end

  def offer_params
    params.require(:offer).permit(:name)
  end
end

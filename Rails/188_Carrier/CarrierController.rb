class CarrierController < ApplicationController
  before_action :set_carrier, only: [:show, :edit, :update, :destroy]

  # GET /carrier
  def index
    @carriers = Carrier.all
    render json: @carriers
  end

  # GET /carrier/1
  def show
    render json: @carrier
  end

  # POST /carrier
  def create
    @carrier = Carrier.new(carrier_params)

    if @carrier.save
      render json: @carrier, status: :created
    else
      render json: @carrier.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /carrier/1
  def update
    if @carrier.update(carrier_params)
      render json: @carrier
    else
      render json: @carrier.errors, status: :unprocessable_entity
    end
  end

  # DELETE /carrier/1
  def destroy
    @carrier.destroy
    head :no_content
  end

  private

  def set_carrier
    @carrier = Carrier.find(params[:id])
  end

  def carrier_params
    params.require(:carrier).permit(:name)
  end
end

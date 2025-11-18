class DistributorController < ApplicationController
  before_action :set_distributor, only: [:show, :edit, :update, :destroy]

  # GET /distributor
  def index
    @distributors = Distributor.all
    render json: @distributors
  end

  # GET /distributor/1
  def show
    render json: @distributor
  end

  # POST /distributor
  def create
    @distributor = Distributor.new(distributor_params)

    if @distributor.save
      render json: @distributor, status: :created
    else
      render json: @distributor.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /distributor/1
  def update
    if @distributor.update(distributor_params)
      render json: @distributor
    else
      render json: @distributor.errors, status: :unprocessable_entity
    end
  end

  # DELETE /distributor/1
  def destroy
    @distributor.destroy
    head :no_content
  end

  private

  def set_distributor
    @distributor = Distributor.find(params[:id])
  end

  def distributor_params
    params.require(:distributor).permit(:name)
  end
end

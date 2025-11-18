class EndpointController < ApplicationController
  before_action :set_endpoint, only: [:show, :edit, :update, :destroy]

  # GET /endpoint
  def index
    @endpoints = Endpoint.all
    render json: @endpoints
  end

  # GET /endpoint/1
  def show
    render json: @endpoint
  end

  # POST /endpoint
  def create
    @endpoint = Endpoint.new(endpoint_params)

    if @endpoint.save
      render json: @endpoint, status: :created
    else
      render json: @endpoint.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /endpoint/1
  def update
    if @endpoint.update(endpoint_params)
      render json: @endpoint
    else
      render json: @endpoint.errors, status: :unprocessable_entity
    end
  end

  # DELETE /endpoint/1
  def destroy
    @endpoint.destroy
    head :no_content
  end

  private

  def set_endpoint
    @endpoint = Endpoint.find(params[:id])
  end

  def endpoint_params
    params.require(:endpoint).permit(:name)
  end
end

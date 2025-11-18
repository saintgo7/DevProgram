class APIController < ApplicationController
  before_action :set_api, only: [:show, :edit, :update, :destroy]

  # GET /api
  def index
    @apis = API.all
    render json: @apis
  end

  # GET /api/1
  def show
    render json: @api
  end

  # POST /api
  def create
    @api = API.new(api_params)

    if @api.save
      render json: @api, status: :created
    else
      render json: @api.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /api/1
  def update
    if @api.update(api_params)
      render json: @api
    else
      render json: @api.errors, status: :unprocessable_entity
    end
  end

  # DELETE /api/1
  def destroy
    @api.destroy
    head :no_content
  end

  private

  def set_api
    @api = API.find(params[:id])
  end

  def api_params
    params.require(:api).permit(:name)
  end
end

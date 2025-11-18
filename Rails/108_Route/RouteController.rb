class RouteController < ApplicationController
  before_action :set_route, only: [:show, :edit, :update, :destroy]

  # GET /route
  def index
    @routes = Route.all
    render json: @routes
  end

  # GET /route/1
  def show
    render json: @route
  end

  # POST /route
  def create
    @route = Route.new(route_params)

    if @route.save
      render json: @route, status: :created
    else
      render json: @route.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /route/1
  def update
    if @route.update(route_params)
      render json: @route
    else
      render json: @route.errors, status: :unprocessable_entity
    end
  end

  # DELETE /route/1
  def destroy
    @route.destroy
    head :no_content
  end

  private

  def set_route
    @route = Route.find(params[:id])
  end

  def route_params
    params.require(:route).permit(:name)
  end
end

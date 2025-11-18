class AuthorizationController < ApplicationController
  before_action :set_authorization, only: [:show, :edit, :update, :destroy]

  # GET /authorization
  def index
    @authorizations = Authorization.all
    render json: @authorizations
  end

  # GET /authorization/1
  def show
    render json: @authorization
  end

  # POST /authorization
  def create
    @authorization = Authorization.new(authorization_params)

    if @authorization.save
      render json: @authorization, status: :created
    else
      render json: @authorization.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /authorization/1
  def update
    if @authorization.update(authorization_params)
      render json: @authorization
    else
      render json: @authorization.errors, status: :unprocessable_entity
    end
  end

  # DELETE /authorization/1
  def destroy
    @authorization.destroy
    head :no_content
  end

  private

  def set_authorization
    @authorization = Authorization.find(params[:id])
  end

  def authorization_params
    params.require(:authorization).permit(:name)
  end
end

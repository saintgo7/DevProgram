class AuthenticationController < ApplicationController
  before_action :set_authentication, only: [:show, :edit, :update, :destroy]

  # GET /authentication
  def index
    @authentications = Authentication.all
    render json: @authentications
  end

  # GET /authentication/1
  def show
    render json: @authentication
  end

  # POST /authentication
  def create
    @authentication = Authentication.new(authentication_params)

    if @authentication.save
      render json: @authentication, status: :created
    else
      render json: @authentication.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /authentication/1
  def update
    if @authentication.update(authentication_params)
      render json: @authentication
    else
      render json: @authentication.errors, status: :unprocessable_entity
    end
  end

  # DELETE /authentication/1
  def destroy
    @authentication.destroy
    head :no_content
  end

  private

  def set_authentication
    @authentication = Authentication.find(params[:id])
  end

  def authentication_params
    params.require(:authentication).permit(:name)
  end
end

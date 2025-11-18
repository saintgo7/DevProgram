class OAuthController < ApplicationController
  before_action :set_oauth, only: [:show, :edit, :update, :destroy]

  # GET /oauth
  def index
    @oauths = OAuth.all
    render json: @oauths
  end

  # GET /oauth/1
  def show
    render json: @oauth
  end

  # POST /oauth
  def create
    @oauth = OAuth.new(oauth_params)

    if @oauth.save
      render json: @oauth, status: :created
    else
      render json: @oauth.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /oauth/1
  def update
    if @oauth.update(oauth_params)
      render json: @oauth
    else
      render json: @oauth.errors, status: :unprocessable_entity
    end
  end

  # DELETE /oauth/1
  def destroy
    @oauth.destroy
    head :no_content
  end

  private

  def set_oauth
    @oauth = OAuth.find(params[:id])
  end

  def oauth_params
    params.require(:oauth).permit(:name)
  end
end
